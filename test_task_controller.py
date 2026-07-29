from app.core.task_controller import (
    create_task_plan,
    create_task_step,
    execute_task_plan,
    print_task_summary,
)


plan = create_task_plan(
    name="Search AI engineering internships",
    steps=[
        create_task_step(
            tool_name="browser.open",
            description="Open Google Chrome",
        ),
        create_task_step(
            tool_name="browser.new_tab",
            description="Create a new Chrome tab",
        ),
        create_task_step(
            tool_name="browser.search",
            arguments={
                "search_text": (
                    "AI engineering internships in India"
                )
            },
            description=(
                "Search for AI engineering internships"
            ),
        ),
    ],
)


result = execute_task_plan(plan)

print_task_summary(result)