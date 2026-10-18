rows = [input()]
while True:
    line = input()
    rows.append(line)
    if line.count('.') == 0 and line.count('~') == 0:
        break

height = len(rows)
width = len(rows[0])

gas = sum(row.count('.') for row in rows)
liquid = sum(row.count('~') for row in rows)

a = height - 2
area = width - 2

gas_rows = gas // a
liquid_rows = area - gas_rows

print(height * '#')
for _ in range(gas_rows):
    print('#' + '.' * a + '#')
for _ in range(liquid_rows):
    print('#' + '~' * a + '#')
print(height * '#')

gas_chunk = round(20 * gas / max(gas, liquid)) if max(gas, liquid) > 0 else 0
liquid_chunk = round(20 * liquid / max(gas, liquid)) if max(gas, liquid) > 0 else 0

gas_text = f'{gas}/{gas + liquid}'
liquid_text = f'{liquid}/{gas + liquid}'
width_text = max(len(gas_text), len(liquid_text))
longest = max(gas_chunk, liquid_chunk)

print('.' * gas_chunk + ' ' * (longest - gas_chunk) + ' ' + gas_text.rjust(width_text))
print('~' * liquid_chunk + ' ' * (longest - liquid_chunk) + ' ' + liquid_text.rjust(width_text))

