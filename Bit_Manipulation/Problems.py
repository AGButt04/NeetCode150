# This file has all the problems in the 1-D Dynamic Programming
# section of the NeetCode150 with the explanations.
import requests
from bs4 import BeautifulSoup

def singleNumber(nums):
    nums.sort()
    single_number = -1
    index = 0

    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            index += 2
        else:
            return nums[index]

    return nums[index]

def hammingWeight(self, n: int) -> int:
    ones = 0

    while n:
        if n & 1 == 1:
            ones += 1
        n >>= 1

    return ones

def countBits(n: int):
    ones_array = [0] * (n + 1)

    for i in range(1, n + 1):
        num = i
        while num != 0:
            ones_array[i] += 1
            num = num & (num - 1)

    return ones_array

def missingNumber(self, nums):
    n = len(nums)
    r_sum = n
    c_sum = 0

    for i, n in enumerate(nums):
        r_sum += i
        c_sum += n

    return r_sum - c_sum

def reverseBits(self, n: int) -> int:
    reverse = 0

    for i in range(32):
        bit = (n >> i) & 1
        reverse += (bit << (31 - i))

    return reverse

def print_secret_message(url):
    # Retrieve the published Google Doc
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if table is None:
        raise ValueError("Could not find a table in the document.")

    grid = {}
    max_x = 0
    max_y = 0

    rows = table.find_all("tr")

    # Skip the header row
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])

        if len(cells) < 3:
            continue

        x = int(cells[0].get_text(strip=True))
        char = cells[1].get_text(strip=True)
        y = int(cells[2].get_text(strip=True))

        grid[(x, y)] = char

        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # y increases upward, so print from largest y down to 0
    for y in range(max_y, -1, -1):
        row_chars = []

        for x in range(max_x + 1):
            row_chars.append(grid.get((x, y), " "))

        print("".join(row_chars))


if __name__ == '__main__':
    print(2 & 1)
    url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

    print_secret_message(url)