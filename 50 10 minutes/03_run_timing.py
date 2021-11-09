def run_time():
    total_time = 0
    count = 0
    while True:
        run_id = input("input run time: ")
        if run_id:
            total_time += int(run_id)
        else:
            break
        count += 1
    print(f'average of {round(total_time/count, 2)}, over {count} runs')


if __name__ == "__main__":
    run_time()
