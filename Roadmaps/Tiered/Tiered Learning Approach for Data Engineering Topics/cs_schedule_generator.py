import datetime

def generate_cs_schedule():
    topics_data = [
        {"name": "Programming", "blocks_total": 24, "blocks_done": 0, "tier": 3, "hours": 20,
         "book": "Structure and Interpretation of Computer Programs (SICP)",
         "videos": "Brian Harvey's SICP lectures (Berkeley CS 61A)"},
        {"name": "Computer Architecture", "blocks_total": 24, "blocks_done": 0, "tier": 3, "hours": 20,
         "book": "Computer Systems: A Programmer's Perspective (CS:APP)",
         "videos": "Berkeley CS 61C"},
        {"name": "Algorithms and Data Structures", "blocks_total": 90, "blocks_done": 0, "tier": 1, "hours": 75,
         "book": "The Algorithm Design Manual (ADM)",
         "videos": "Steven Skiena's lectures"},
        {"name": "Operating Systems", "blocks_total": 45, "blocks_done": 0, "tier": 2, "hours": 37.5,
         "book": "Operating Systems: Three Easy Pieces (OSTEP)",
         "videos": "Berkeley CS 162"},
        {"name": "Computer Networking", "blocks_total": 45, "blocks_done": 0, "tier": 2, "hours": 37.5,
         "book": "Computer Networking: A Top-Down Approach",
         "videos": "Stanford CS 144"},
        {"name": "Databases", "blocks_total": 90, "blocks_done": 0, "tier": 1, "hours": 75,
         "book": "Readings in Database Systems (Red Book)",
         "videos": "Joe Hellerstein's Berkeley CS 186"}
    ]

    start_date = datetime.date(2025, 12, 1)  # Monday
    current_date = start_date
    week_number = 0
    
    schedule_md = "# Computer Science Foundations Roadmap for Data Engineers (TYCS Aligned)\n\n"
    schedule_md += "## Plan Overview\n\n"
    schedule_md += "- **Start Date**: December 1, 2025 (Monday)\n"
    schedule_md += "- **Weekly Structure**: 13 study blocks per week (1 block = 50 minutes).\n"
    schedule_md += "  - Saturday - Thursday: 2 blocks/day\n"
    schedule_md += "  - Friday: 1 block/day\n"
    schedule_md += "- **First Week (Dec 1 - Dec 5, 2025)**: 5 days, 9 study blocks.\n"
    schedule_md += "  - Monday - Thursday: 2 blocks/day\n"
    schedule_md += "  - Friday: 1 block/day\n"
    schedule_md += "- **Resources**: Primarily from [Teach Yourself Computer Science](https://teachyourselfcs.com/)\n\n"
    schedule_md += "## Tiered Hour Allocation & Topics\n\n"
    schedule_md += "The following topics are ordered according to TYCS recommendations for the subjects you selected. The hours are distributed based on your tiered investment approach:\n\n"
    schedule_md += "- **Tier 3 (Pragmatic Investment: 40 hours total)**\n"
    schedule_md += "  - Programming: 20 hours (24 blocks) - Book: Structure and Interpretation of Computer Programs, Videos: Brian Harvey's SICP lectures\n"
    schedule_md += "  - Computer Architecture: 20 hours (24 blocks) - Book: Computer Systems: A Programmer's Perspective, Videos: Berkeley CS 61C\n"
    schedule_md += "- **Tier 1 (Full Investment: 150 hours total)**\n"
    schedule_md += "  - Algorithms & Data Structures: 75 hours (90 blocks) - Book: The Algorithm Design Manual, Videos: Steven Skiena's lectures\n"
    schedule_md += "  - Databases: 75 hours (90 blocks) - Book: Readings in Database Systems, Videos: Joe Hellerstein's Berkeley CS 186\n"
    schedule_md += "- **Tier 2 (Focused Investment: 75 hours total)**\n"
    schedule_md += "  - Operating Systems: 37.5 hours (45 blocks) - Book: Operating Systems: Three Easy Pieces, Videos: Berkeley CS 162\n"
    schedule_md += "  - Computer Networking: 37.5 hours (45 blocks) - Book: Computer Networking: A Top-Down Approach, Videos: Stanford CS 144\n\n"
    schedule_md += "## Detailed Weekly Schedule\n\n"

    days_of_week_first_map = [
        ("Monday", 2), ("Tuesday", 2), ("Wednesday", 2), ("Thursday", 2), ("Friday", 1)
    ]

    days_of_week_full_map = [
        ("Saturday", 2), ("Sunday", 2), ("Monday", 2), ("Tuesday", 2), 
        ("Wednesday", 2), ("Thursday", 2), ("Friday", 1)
    ]

    current_topic_idx = 0
    all_topics_done = False

    while not all_topics_done:
        week_number += 1
        is_first_week = (week_number == 1)
        
        week_start_date_str = current_date.strftime("%B %d, %Y")
        
        if is_first_week:
            days_in_week = 5
            week_end_date = current_date + datetime.timedelta(days=days_in_week - 1)
            current_week_day_map = days_of_week_first_map
            blocks_available_this_week = 9
        else:
            days_in_week = 7
            week_end_date = current_date + datetime.timedelta(days=days_in_week - 1)
            current_week_day_map = days_of_week_full_map
            blocks_available_this_week = 13

        week_end_date_str = week_end_date.strftime("%B %d, %Y")
        
        schedule_md += f"### Week {week_number}: {week_start_date_str} - {week_end_date_str} ({blocks_available_this_week} blocks)\n"
        schedule_md += "| Day       | Date       | Blocks | Focus Topic(s) |\n"
        schedule_md += "|-----------|------------|--------|----------------|\n"

        day_date_iter = current_date
        topics_in_week_summary = [] # Tracks unique topic names for the week's summary
        topic_progress_in_week = {} # Tracks blocks done for each topic within this week for summary

        for day_idx, (day_name, daily_blocks_total) in enumerate(current_week_day_map):
            day_date_str = day_date_iter.strftime("%b %d")
            focus_for_day_details = []
            blocks_remaining_for_day = daily_blocks_total
            
            while blocks_remaining_for_day > 0 and current_topic_idx < len(topics_data):
                topic = topics_data[current_topic_idx]
                if topic['name'] not in topic_progress_in_week:
                    topic_progress_in_week[topic['name']] = {'done_this_week': 0, 'total_at_week_start': topic['blocks_done']}
                
                if topic["blocks_done"] < topic["blocks_total"]:
                    if topic["name"] not in topics_in_week_summary:
                        topics_in_week_summary.append(topic["name"])

                    blocks_to_do_for_topic_today = min(
                        blocks_remaining_for_day, 
                        topic["blocks_total"] - topic["blocks_done"]
                    )
                    
                    focus_for_day_details.append(f"{topic['name']} ({blocks_to_do_for_topic_today} blk)")
                    
                    topic["blocks_done"] += blocks_to_do_for_topic_today
                    topic_progress_in_week[topic['name']]['done_this_week'] += blocks_to_do_for_topic_today
                    blocks_remaining_for_day -= blocks_to_do_for_topic_today

                    if topic["blocks_done"] == topic["blocks_total"]:
                        current_topic_idx += 1 
                else:
                    current_topic_idx += 1
                    if current_topic_idx < len(topics_data):
                         # Ensure new topic is initialized for progress tracking if it starts mid-day/week
                        new_topic_for_day = topics_data[current_topic_idx]
                        if new_topic_for_day['name'] not in topic_progress_in_week:
                            topic_progress_in_week[new_topic_for_day['name']] = {'done_this_week': 0, 'total_at_week_start': new_topic_for_day['blocks_done']}
                    continue
            
            schedule_md += f"| {day_name:<9} | {day_date_str:<10} | {daily_blocks_total:<6} | {', '.join(focus_for_day_details) if focus_for_day_details else 'Rest/Catch-up'} |\n"
            day_date_iter += datetime.timedelta(days=1)
        
        if topics_in_week_summary:
             schedule_md += f"\n*Focus this week: {', '.join(topics_in_week_summary)}*\n"
        for topic_name_summary in topics_in_week_summary: # Iterate in order they appeared
            # Find the topic data by name to get its total blocks
            original_topic_data = next(t for t in topics_data if t['name'] == topic_name_summary)
            total_blocks_for_this_topic = original_topic_data['blocks_total']
            # total_done_by_end_of_week = topic_progress_in_week[topic_name_summary]['total_at_week_start'] + topic_progress_in_week[topic_name_summary]['done_this_week']
            total_done_by_end_of_week = original_topic_data['blocks_done'] # This is simpler and already updated
            schedule_md += f"  - {topic_name_summary}: {topic_progress_in_week[topic_name_summary]['done_this_week']} blocks studied this week. (Total progress: {total_done_by_end_of_week}/{total_blocks_for_this_topic} blocks)\n"
        schedule_md += "\n"

        all_topics_done = True
        for topic_check in topics_data:
            if topic_check["blocks_done"] < topic_check["blocks_total"]:
                all_topics_done = False
                break
        
        if all_topics_done:
            break

        current_date = week_end_date + datetime.timedelta(days=1)

    total_weeks_actual = week_number

    schedule_md += f"\n## Note on Topic Selection\n\n"
    schedule_md += "This roadmap focuses on the 6 topics you prioritized for your data engineering path, ordered according to the general structure of [Teach Yourself Computer Science](https://teachyourselfcs.com/).\n"
    schedule_md += "The original TYCS guide lists 9 subjects. The topics *not* included in this specific plan are:\n"
    schedule_md += "- Math for CS\n"
    schedule_md += "- Languages and Compilers\n"
    schedule_md += "- Distributed Systems\n\n"
    schedule_md += "You can consider these for future study if desired. The hour allocations for the selected topics have been mapped to your specified Tier 1 (150h), Tier 2 (75h), and Tier 3 (40h) investment levels.\n"
    schedule_md += f"\n**Estimated total duration: {total_weeks_actual} weeks.**\n"

    return schedule_md

if __name__ == "__main__":
    # This part is for local testing and won't be run by the shell_exec directly
    # To get the output, the agent will need to import and call generate_cs_schedule()
    # and print the result.
    # For now, the agent will just write this script to a file.
    # The next step would be to execute it and capture output.
    pass

