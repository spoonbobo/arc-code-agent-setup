import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Show available actions for an ARC-AGI game",
  args: {
    game_id: tool.schema.string().describe("Game ID (e.g., ls20-cb3b57cc)"),
    mode: tool.schema.enum(["normal", "online", "offline"]).optional().describe("Operation mode (default: normal)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const script = path.join(context.worktree, ".opencode/scripts/arc_show_actions.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script} --game-id ${args.game_id} --mode ${mode}`.text()
    return result.trim()
  },
})
