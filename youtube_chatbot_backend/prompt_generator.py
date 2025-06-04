from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template=(
        'You are AI assistant.'
        'Based on "context" from a video transcript, answer the user\'s "query".\n'
        '{{"context": "{transcript_context}", "query": "{user_input}"}}\n'
        'Answer:'
    ),
    input_variables=['transcript_context','user_input'],
    validate_template=True
)

template.save('template.json')