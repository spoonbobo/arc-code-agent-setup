import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Quick play an ARC-AGI game",
  args: {
    game_id: tool.schema.string().optional().describe("Game ID (auto-discovers if not provided)"),
    mode: tool.schema.enum(["normal", "online", "offline"]).optional().describe("Operation mode (default: normal)"),
    steps: tool.schema.number().optional().describe("Number of steps (default: 10)"),
    render: tool.schema.boolean().optional().describe("Enable terminal rendering (default: false)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const steps = args.steps || 10
    const render = args.render || false
    
    let cmd = `cd ${context.worktree} && uv run python launch.py`
    
    if (args.game_id) {
      cmd = `ARC_GAME_ID=${args.game_id} ${cmd}`
    }
    if (mode !== "normal") {
      cmd = `ARC_OPERATION_MODE=${mode} ${cmd}`
    }
    
    const result = await Bun.$`${cmd}`.text()
    return result.trim()
  },
})
