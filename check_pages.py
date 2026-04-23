import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all <section class="page..." id="page-...">
page_ids = re.findall(r'<section[^>]+class="[^"]*page[^"]*"[^>]+id="page-([^"]+)"', content)
print("Page IDs found in HTML:")
for pid in page_ids:
    print(f" - {pid}")

# Find all goPage('...') calls
gopage_calls = re.findall(r"goPage\('([^']+)'\)", content)
print("\ngoPage calls found in HTML:")
for call in set(gopage_calls):
    print(f" - {call}")

# Check for mismatches
for call in set(gopage_calls):
    if call not in page_ids:
        print(f"\nMISMATCH: goPage('{call}') has no corresponding <section id='page-{call}'>")
