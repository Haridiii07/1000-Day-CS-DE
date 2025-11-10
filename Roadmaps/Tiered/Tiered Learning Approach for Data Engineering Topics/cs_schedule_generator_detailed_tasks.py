import datetime

# Illustrative tasks for each topic
# For brevity in this script, task descriptions are generic.
# The user MUST refer to the detailed *_tasks_full.md files for actual task details for each block.
programming_tasks = [f"Programming Task {i+1}/48 (See programming_tasks_full.md)" for i in range(48)]
architecture_tasks = [f"CompArch Task {i+1}/48 (See computer_architecture_tasks_full.md)" for i in range(48)]
algorithms_tasks = [f"Algo/DS Task {i+1}/180 (See algorithms_tasks_full.md)" for i in range(180)]
os_tasks = [f"OS Task {i+1}/90 (See operating_systems_tasks_full.md)" for i in range(90)]
networking_tasks = [f"Networking Task {i+1}/90 (See computer_networking_tasks_full.md)" for i in range(90)]
databases_tasks = [f"Databases Task {i+1}/180 (See databases_tasks_full.md)" for i in range(180)]

topics_data = [
    {"name": "Programming", "blocks_total": 48, "tier": 3, "resources": "SICP & Harvey Lectures", "tasks": programming_tasks},
    {"name": "Computer Architecture", "blocks_total": 48, "tier": 3, "resources": "CS:APP & Berkeley CS 61C", "tasks": architecture_tasks},
    {"name": "Algorithms & Data Structures", "blocks_total": 180, "tier": 1, "resources": "ADM & Skiena Lectures", "tasks": algorithms_tasks},
    {"name": "Operating Systems", "blocks_total": 90, "tier": 2, "resources": "OSTEP & Berkeley CS 162", "tasks": os_tasks},
    {"name": "Computer Networking", "blocks_total": 90, "tier": 2, "resources": "CN: Top-Down & Stanford CS 144", "tasks": networking_tasks},
    {"name": "Databases", "blocks_total": 180, "tier": 1, "resources": "Red Book & Berkeley CS 186", "tasks": databases_tasks},
]

def generate_schedule(start_date_str, weekly_blocks_total, topics):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    current_date = start_date
    
    schedule_md = "# Tiered CS Study Schedule with Detailed Tasks\n\n"
    schedule_md += "**Important Note:** This schedule lists placeholder task descriptions (e.g., \"Prog Task 1/48\"). "
    schedule_md += "You **MUST** refer to the correspondingly named `*_tasks_full.md` files (e.g., `programming_tasks_full.md`) "
    schedule_md += "for the actual detailed activities, readings, and exercises for each study block.\n\n"
    schedule_md += "This schedule focuses on the 6 topics you prioritized for your data engineering path, drawing from the 9 topics recommended by TeachYourselfCS. The time allocations reflect your tiered approach.\n\n"

    # Initialize remaining blocks and task counters for each topic
    remaining_blocks = {topic["name"]: topic["blocks_total"] for topic in topics}
    topic_task_counters = {topic["name"]: 0 for topic in topics}
    total_blocks_to_schedule = sum(topic["blocks_total"] for topic in topics)
    blocks_scheduled_count = 0
    
    week_number = 0

    # Sort topics by tier first, then by original order if tiers are same (for initial picking)
    # For simplicity in this version, we will iterate through topics as provided and fill them.
    # A more complex logic would interleave topics based on tier or user preference for variety.
    
    current_topic_index = 0

    while blocks_scheduled_count < total_blocks_to_schedule:
        week_number += 1
        week_start_date = current_date
        days_in_this_week = 5 if week_number == 1 else 7 # First week Mon-Fri, then Sat-Fri
        week_end_date = week_start_date + datetime.timedelta(days=days_in_this_week - 1)
        schedule_md += "| Day       | Date       | Blocks | Focus for the Day (Refer to detailed task files) |\n"
        schedule_md += "|-----------|------------|--------|----------------------------------------------------|\n"
        
        daily_blocks_distribution = [2, 2, 2, 2, 1] if week_number == 1 else [2, 2, 2, 2, 2, 2, 1] # Mon-Fri or Sat-Thu, Fri
        week_days_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] if week_number == 1 else ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        topics_in_week_summary = set()

        for i in range(days_in_this_week):
            day_date = week_start_date + datetime.timedelta(days=i)
            day_name = week_days_names[i]
            daily_blocks_total = daily_blocks_distribution[i]
            blocks_for_day_done = 0
            focus_for_day_details = []

            while blocks_for_day_done < daily_blocks_total and blocks_scheduled_count < total_blocks_to_schedule:
                # Find the current topic to work on
                # Simple round-robin through topics that still have blocks
                topic_found = False
                for _ in range(len(topics)):
                    topic = topics[current_topic_index]
                    if remaining_blocks[topic["name"]] > 0:
                        topic_found = True
                        break
                    current_topic_index = (current_topic_index + 1) % len(topics)
                
                if not topic_found: # Should not happen if total_blocks_to_schedule is managed correctly
                    break

                blocks_to_do_for_topic_today = min(daily_blocks_total - blocks_for_day_done, remaining_blocks[topic["name"]])
                
                task_list_for_topic = topic.get("tasks", [])
                task_counter_for_topic = topic_task_counters[topic["name"]]
                
                task_description = f"{topic['name']} (Block {topic['blocks_total'] - remaining_blocks[topic['name']] + 1})"
                if task_counter_for_topic < len(task_list_for_topic):
                    task_description = task_list_for_topic[task_counter_for_topic]
                    topic_task_counters[topic["name"]] += 1
                
                focus_for_day_details.append(f"{task_description}")
                
                remaining_blocks[topic["name"]] -= 1
                blocks_for_day_done += 1
                blocks_scheduled_count += 1
                topics_in_week_summary.add(topic["name"])
                
                if remaining_blocks[topic["name"]] == 0:
                     # Move to next topic if current one is finished for the day or overall
                    current_topic_index = (current_topic_index + 1) % len(topics)
                
                if blocks_for_day_done == daily_blocks_total or blocks_scheduled_count == total_blocks_to_schedule:
                    break # Move to next day or finish scheduling
            
            schedule_md += f"| {day_name:<9} | {day_date.strftime('%Y-%m-%d'):<10} | {blocks_for_day_done:<6} | {'; '.join(focus_for_day_details) if focus_for_day_details else 'Rest/Catch-up'} |\n"
            current_date = day_date + datetime.timedelta(days=1)
        
        if topics_in_week_summary:
             joined_topics_summary = ", ".join(sorted(list(topics_in_week_summary)))
             schedule_md += f"\n*Focus this week includes: {joined_topics_summary}*\n"
        schedule_md += "\n---\n\n"

    schedule_md += "## All Topics Scheduled!\n"
    schedule_md += f"Total blocks scheduled: {blocks_scheduled_count}\n"
    schedule_md += "Review the detailed `*_tasks_full.md` files for each topic to understand the specific activities for each block listed above.\n"
    return schedule_md

if __name__ == "__main__":
    # User-defined parameters
    study_start_date = "2025-12-01" # Monday
    total_weekly_blocks = 13

    # Sort topics by tier for scheduling priority (Tier 1 first)
    # Within the same tier, maintain the original order or define a sub-order if needed.
    # For this script, we'll use a simplified approach of filling one topic then moving to the next for demonstration.
    # A more complex scheduler might interleave topics more dynamically.
    # For now, the order in topics_data will be used sequentially.
    
    # For the purpose of this script, we'll use the topics_data as defined globally.
    # A more robust script might pass it as an argument or load from a config.
    
    generated_markdown_schedule = generate_schedule(study_start_date, total_weekly_blocks, topics_data)
    print(generated_markdown_schedule)

