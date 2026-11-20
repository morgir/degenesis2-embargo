// Kompiluje źródła kompendiów (src/packs/*/*.json) do baz LevelDB w packs/.
import { compilePack } from "@foundryvtt/foundryvtt-cli";
import fs from "node:fs";
import path from "node:path";
const root = path.resolve(import.meta.dirname, "..");
const src = path.join(root, "src/packs"), dst = path.join(root, "packs");
fs.rmSync(dst, { recursive: true, force: true });
for (const name of fs.readdirSync(src)) {
  await compilePack(path.join(src, name), path.join(dst, name), { log: false, recursive: false });
  console.log("skompilowano", name);
}
