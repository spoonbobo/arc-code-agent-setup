import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Play an ARC-AGI game with recording enabled",
  args: {
    game_id: tool.schema.string().describe("Game ID (e.g., ls20-cb3b57cc)"),
    mode: tool.schema.enum(["normal", "online", "offline"]).optional().describe("Operation mode (default: normal)"),
    steps: tool.schema.number().optional().describe("Number of steps (default: 10)"),
    render: tool.schema.boolean().optional().describe("Enable terminal rendering (default: false)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const steps = args.steps || 10
    const script = path.join(context.worktree, ".opencode/scripts/arc_play_with_recording.py")
    let cmd = `cd ${context.worktree} && uv run python ${script} --game-id ${args.game_id} --mode ${mode} --steps ${steps}`
    
    if (args.render) {
      cmd += ` --render`
    }
    
    const result = await Bun.$`${cmd}`.text()
    return result.trim()
  },
})
