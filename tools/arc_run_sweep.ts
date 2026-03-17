import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Run a sweep of the same ARC-AGI game with different random seeds",
  args: {
    game_id: tool.schema.string().describe("Game ID (e.g., ls20-cb3b57cc)"),
    mode: tool.schema.enum(["normal", "online", "offline"]).optional().describe("Operation mode (default: normal)"),
    runs: tool.schema.number().optional().describe("Number of runs (default: 5)"),
    steps: tool.schema.number().optional().describe("Steps per run (default: 10)"),
  },
  async execute(args, context) {
    const mode = args.mode || "normal"
    const runs = args.runs || 5
    const steps = args.steps || 10
    const script = path.join(context.worktree, ".opencode/scripts/arc_run_sweep.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script} --game-id ${args.game_id} --mode ${mode} --runs ${runs} --steps ${steps}`.text()
    return result.trim()
  },
})
