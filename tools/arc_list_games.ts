import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "List available ARC-AGI games",
  args: {
    mode: tool.schema.enum(["normal", "online", "offline"]).optional().describe("Operation mode (default: normal)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const script = path.join(context.worktree, ".opencode/scripts/arc_list_games.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script} --mode ${mode}`.text()
    return result.trim()
  },
})
