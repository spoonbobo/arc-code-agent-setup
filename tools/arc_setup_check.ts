import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Check ARC-AGI setup (API key, config, cached games)",
  args: {},
  async execute(args, context) {
    const script = path.join(context.worktree, ".opencode/scripts/arc_setup_check.py")
    const result = await Bun.$`cd ${context.worktree} && uv run python ${script}`.text()
    return result.trim()
  },
})
