with open('frontend/index.html','rb') as f:
    h = f.read().decode('utf-8','replace')

start = h.index('<script>') + 8
end = h.rindex('</script>')
script = h[start:end]
lines = script.split('\n')

# For each actual line, count how many visual lines it would take
# VS Code default word wrap = window width, approx 120 chars
wrap = 120
visual_line = 0
for i, l in enumerate(lines):
    l_len = len(l.rstrip())
    visual_lines = max(1, (l_len + wrap - 1) // wrap)
    prev_visual = visual_line
    visual_line += visual_lines
    # VS Code Problems panel "Ln 2576" - actual file line includes the HTML before script
    # Script starts at actual line 695
    actual_line = 695 + i
    if prev_visual <= 2576 - 695 <= visual_line:
        print(f'ERROR LIKELY IN ACTUAL LINE {actual_line} (script line {i+1})')
        print(f'Visual lines {prev_visual+695} to {visual_line+695}')
        print('Content:', l[:200])
        break

# Also check for the specific column 2134 
# Find lines longer than 2134 chars
print('\nLines longer than 2134 chars:')
for i, l in enumerate(lines):
    if len(l) > 2134:
        actual = 695 + i
        print(f'  Script line {i+1} (HTML line {actual}): {len(l)} chars')
        # Check around col 2134
        print(f'  Around col 2134: ...{l[2100:2160]}...')
