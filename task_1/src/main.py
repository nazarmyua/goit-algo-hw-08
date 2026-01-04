import heapq


def min_merge_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


def main():
    cables = [4, 3, 2, 6, 9]
    min_cost = min_merge_cost(cables)
    print(f"Min merge cost: {min_cost}")


if __name__ == "__main__":
    main()
