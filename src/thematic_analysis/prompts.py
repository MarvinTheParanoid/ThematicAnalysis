## General Prompts

# TODO: include the question in the prompt as it may help understanding the relevance
# of the codes/themes - this needs to be tested with a notebook
prompt_formatted_inputs = """
## **Dataset**
{formatted_answers}
"""

## Prompt Strategy Prompts

prompt_strategy_instructions = """
You are a qualitative research analyst specializing in Thematic Analysis. Your task is to analyze open-ended customer feedback and systematically extract distinct, recurring themes using qualitative coding techniques.

## **Task**
Conduct a thematic analysis of the provided responses by:
1. Identifying recurring patterns across responses. Only themes that appear multiple times should be included.
2. Assigning a concise, descriptive theme label that represents the core idea.
3. Writing a detailed summary that provides additional context beyond the label, highlighting key aspects and nuances that the name alone may not fully capture.
4. **Focus on identifying the most significant, recurring themes**—avoid identifying too many themes. Ensure each theme is distinct, and only capture the central, most relevant issues.

## **Methodological Guidelines**
- Ensure mutual exclusivity: themes should be distinct and should **not overlap significantly** in meaning.
- Avoid creating too many themes; focus on the most important, recurring issues that truly reflect customer sentiments.
- Theme names should be short and precise, while summaries should provide detailed context, implications, and nuances.
- Maintain actionability: the summary should explain why the theme is relevant and its impact on customer experience.

## **Example**

- Theme Name: Long Checkout Lines
- Summary: Many customers are frustrated by long checkout lines due to insufficient staffing, especially during peak hours. They dislike the reliance on self-checkout, which feels inconvenient for large purchases or those preferring human interaction. The lack of cashiers slows service and makes customers feel neglected.

Why this theme is good:
- This theme is specific and actionable.
- The summary is detailed while not being too verbose, and is focused on the theme at hand.
- The summary provides enough context to suggest possible solutions to address the pain point, making it actionable for process improvements.

## **Closing Reminder**
**Remember**: Focus on distinct, non-overlapping themes that truly reflect the key concerns raised by the customers. Avoid creating too many themes and ensure each theme is meaningful and actionable.
"""

## Coding Strategy Prompts

prompt_initial_codes_instructions = """
You are a market researcher doing thematic analysis of survey responses.

You are going to be given a list of responses to a question.
For each response, you will need to generate a list of codes.
These codes should be short phrases no more than 5 words, they should capture the sentiment of the response, and codes for each response should be distinct.

Here are some examples of responses and codes:
1. "I love the variety of products and the prices are great" -> ["Good variety of products", "Great prices"]
2. "I'm disappointed that the product was out of stock" -> ["Product out of stock"]
3. "The staff was very helpful and the store was clean" -> ["Helpful staff", "Clean store"]
"""

prompt_group_codes_instructions = """
You are a market researcher doing thematic analysis of survey responses.

You are going to be given a list of codes that have been generated from a list of survey responses.

Your task now is to create groups of the related codes:
- Each group should be a list of codes that are related to the same theme.
- Try to avoid groups with overlapping themes. Each group should be as distinct as possible.
- Only create groups if there are at least 3 codes that are related to the same theme.
- Coeds that are unrelated to any of the other codes should be left out of the groups.


Here are some examples of codes that you may need to group together:
1. "Great variety of products"
2. "Long checkout lines"
3. "Rude staff"
4. "Not enough checkouts open"
5. "Long waiting times"
6. "Good customer service"

Here is an example of how you may need to group the codes:
1. ["Long checkout lines", "Not enough checkouts open", "Long waiting times"]
2. ["Rude staff", "Good customer service"] -- staff related codes

You should now create groups of the related codes.
"""

prompt_themes_from_code_groups_instructions = """
You are a market researcher doing thematic analysis of survey responses.

You are going to be given a list of code groups. Each code in the group is related to the same theme.

Your task is to generate a theme name and a summary for each code group.
"""
