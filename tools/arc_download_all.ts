import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Download all available ARC-AGI games for offline use",
  args: {
    mode: tool.schema.enum(["normal", "online"]).optional().describe("Operation mode (default: normal)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const script = path.join(context.worktree, ".opencode/scripts/arc_download_all.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script} --mode ${mode}`.text()
    return result.trim()
  },
})
