import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Download a specific ARC-AGI game for offline use",
  args: {
    game_id: tool.schema.string().describe("Game ID to download (e.g., ls20-cb3b57cc)"),
    mode: tool.schema.enum(["normal", "online"]).optional().describe("Operation mode (default: normal)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const script = path.join(context.worktree, ".opencode/scripts/arc_download_game.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script} --game-id ${args.game_id} --mode ${mode}`.text()
    return result.trim()
  },
})
