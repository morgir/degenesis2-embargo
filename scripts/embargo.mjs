/**
 * Degenesis 2.0 — Embargo: import przygody do świata jednym przyciskiem.
 * Zachowuje ID dokumentów (aktualizacja nie tworzy duplikatów) i strukturę folderów z kompendiów.
 */
const MOD = "degenesis2-embargo";
const PACKS = ["dzienniki", "aktorzy", "sceny"];

Hooks.once("init", () => {
  game.settings.register(MOD, "installedVersion", { scope: "world", config: false, type: String, default: "" });
});

Hooks.once("ready", async () => {
  if (!game.user.isGM) return;
  game.modules.get(MOD).api = { install: openDialog };
  const inst = game.settings.get(MOD, "installedVersion");
  const ver = game.modules.get(MOD).version;
  if (!inst || foundry.utils.isNewerVersion(ver, inst)) openDialog({ update: inst || null });
});

Hooks.on("renderJournalDirectory", (app, html) => {
  if (!game.user.isGM) return;
  const root = html instanceof HTMLElement ? html : html[0];
  const target = root?.querySelector(".header-actions");
  if (!target || target.querySelector(".d2e-btn")) return;
  const b = document.createElement("button");
  b.type = "button"; b.className = "d2e-btn"; b.style.flex = "1 1 100%";
  b.innerHTML = `<i class="fa-solid fa-file-import"></i> Embargo — importuj`;
  b.addEventListener("click", () => openDialog());
  target.append(b);
});

async function openDialog({ update = null } = {}) {
  const { DialogV2 } = foundry.applications.api;
  const intro = update
    ? `<p>Moduł zaktualizowano z <b>${update}</b> do <b>${game.modules.get(MOD).version}</b>. Doinstalować nową zawartość?</p>`
    : `<p>Zaimportować przygodę <b>Embargo</b> do świata? Dzienniki, aktorzy i sceny trafią do folderów „Embargo”. Handouty od razu będą widoczne dla graczy.</p>`;
  const res = await DialogV2.wait({
    window: { title: "Degenesis 2.0 — Embargo", icon: "fa-solid fa-file-import" },
    content: `${intro}<label style="display:flex;gap:6px;align-items:center"><input type="checkbox" name="overwrite"> Nadpisz to, co już jest w świecie (utracisz własne zmiany)</label>
      <label style="display:flex;gap:6px;align-items:center"><input type="checkbox" name="open" ${update ? "" : "checked"}> Otwórz przygodę i aktywuj scenę „Tumbler — osada”</label>`,
    buttons: [
      { action: "ok", label: "Importuj", icon: "fa-solid fa-download", default: true,
        callback: (e, b) => ({ overwrite: b.form.elements.overwrite.checked, open: b.form.elements.open.checked }) },
      { action: "later", label: "Później" },
      { action: "never", label: "Nie pytaj" }
    ],
    rejectClose: false
  });
  if (res === "never") return game.settings.set(MOD, "installedVersion", game.modules.get(MOD).version);
  if (!res || res === "later") return;
  const n = [];
  for (const p of PACKS) n.push(await importPack(game.packs.get(`${MOD}.${p}`), res.overwrite));
  await game.settings.set(MOD, "installedVersion", game.modules.get(MOD).version);
  ui.notifications.info(`Embargo: zaimportowano ${n.reduce((a, b) => a + b, 0)} dokumentów.`);
  if (res.open) {
    game.journal.find(j => j.name === "Embargo — przygoda (MG)")?.sheet.render(true);
    const sc = game.scenes.find(s => s.name === "Tumbler — osada");
    if (sc) await sc.activate();
  }
}

async function importPack(pack, overwrite) {
  if (!pack) return 0;
  const type = pack.documentName;
  const coll = game.collections.get(type);
  const fmap = {};
  const folders = [...(pack.folders ?? [])].sort((a, b) => (a.ancestors?.length ?? 0) - (b.ancestors?.length ?? 0));
  for (const f of folders) {
    const parent = f.folder ? fmap[f.folder.id ?? f.folder] ?? null : null;
    let wf = game.folders.find(x => x.type === type && x.name === f.name && (x.folder?.id ?? null) === parent);
    if (!wf) wf = await Folder.create({ name: f.name, type, folder: parent, color: f.color, sorting: f.sorting ?? "m", sort: f.sort });
    fmap[f.id] = wf.id;
  }
  const docs = await pack.getDocuments();
  const create = [], replace = [];
  for (const d of docs) {
    const data = coll.fromCompendium(d, { keepId: true, clearFolder: true, clearOwnership: false });
    data.folder = fmap[d._source.folder] ?? null;
    if (coll.has(d.id)) { if (overwrite) replace.push(data); } else create.push(data);
  }
  const cls = CONFIG[type].documentClass;
  if (replace.length) { await cls.deleteDocuments(replace.map(d => d._id)); await cls.createDocuments(replace, { keepId: true }); }
  if (create.length) await cls.createDocuments(create, { keepId: true });
  return create.length + replace.length;
}
