n, m = map(int, input().strip().split())

site_dict = {}

for _ in range(n):
    site, password = input().strip().split()
    site_dict[site] = password

for _ in range(m):
    site = input().strip()
    print(site_dict[site])