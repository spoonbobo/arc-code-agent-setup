import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Get ARC-AGI scorecard results",
  args: {
    scorecard_id: tool.schema.string().optional().describe("Scorecard ID (default: current active)"),
    json: tool.schema.boolean().optional().describe("Output full JSON (default: false)"),
  },
  async execute(args, context) {
    const script = path.join(context.worktree, ".opencode/scripts/arc_get_scorecard.py")
    let cmd = `cd ${context.worktree} && uv run python ${script}`
    
    if (args.scorecard_id) {
      cmd += ` --scorecard-id ${args.scorecard_id}`
    }
    if (args.json) {
      cmd += ` --json`
    }
    
    const result = await Bun.$`${cmd}`.text()
    return result.trim()
  },
})
