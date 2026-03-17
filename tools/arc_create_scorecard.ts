import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Create a custom ARC-AGI scorecard with tags and metadata",
  args: {
    tags: tool.schema.array(tool.schema.string()).optional().describe("Tags for the scorecard (e.g., ['experiment', 'v1'])"),
    source_url: tool.schema.string().optional().describe("Source URL (e.g., git repository link)"),
    opaque: tool.schema.string().optional().describe("JSON string for custom opaque data"),
  },
  async execute(args, context) {
    const script = path.join(context.worktree, ".opencode/scripts/arc_create_scorecard.py")
    let cmd = `cd ${context.worktree} && uv run python ${script}`
    
    if (args.tags && args.tags.length > 0) {
      cmd += ` --tags ${args.tags.join(" ")}`
    }
    if (args.source_url) {
      cmd += ` --source-url "${args.source_url}"`
    }
    if (args.opaque) {
      cmd += ` --opaque '${args.opaque}'`
    }
    
    const result = await Bun.$`${cmd}`.text()
    return result.trim()
  },
})
