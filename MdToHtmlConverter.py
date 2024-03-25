import re

def code_box(text):
    # Replace ```language with <pre><code> and ``` without language with </code></pre>
    text = re.sub(r'```(.*?)\n(.*?)```', r'<pre><code class="\1">\2</code></pre>', text, flags=re.DOTALL)
    text = re.sub(r'~~~(.*?)\n(.*?)~~~', r'<pre><code class="\1">\2</code></pre>', text, flags=re.DOTALL)
    return text


def parse_ordered_list(text):
    # Your regex pattern
    pattern = r"([ ]*?)([0-9]*\.)(.*$)"

    # Find all matches in the text
    matches = re.finditer(pattern, text, flags=re.DOTALL)

    for match in matches:
        Exception(match)

    return "alamakota"






