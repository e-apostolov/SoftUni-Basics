pool_volume = int(input())
pipe_1_throughput = int(input())
pipe_2_throughput = int(input())
time = float(input())

pipe_1_volume = pipe_1_throughput * time
pipe_2_volume = pipe_2_throughput * time
total_volume = pipe_1_volume + pipe_2_volume

if pool_volume >= total_volume:
    print(f"The pool is {(total_volume / pool_volume) * 100:.2f}% full. Pipe 1: {(pipe_1_volume / total_volume) * 100:.2f}%. Pipe 2: {(pipe_2_volume / total_volume) * 100:.2f}%.")
else:
    print(f"For {time:.2f} hours the pool overflows with {abs(total_volume - pool_volume):.2f} liters.")