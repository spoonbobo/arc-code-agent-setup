import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Inspect an ARC-AGI game (show metadata and available actions without playing)",
  args: {
    game_id: tool.schema.string().describe("Game ID to inspect (e.g., ls20-cb3b57cc)"),
    mode: tool.schema.enum(["normal", "online", "offline"]).optional().describe("Operation mode (default: normal)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const script = path.join(context.worktree, ".opencode/scripts/arc_inspect_game.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script} --game-id ${args.game_id} --mode ${mode}`.text()
    return result.trim()
  },
})
