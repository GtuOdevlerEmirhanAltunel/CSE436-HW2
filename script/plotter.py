import matplotlib.pyplot as plt
import numpy as np
import sys

# Load data, assuming it starts with a header line and space-separated columns.
data = np.loadtxt(sys.argv[1])

# Extract columns: typically the first is time, and the others are signals like
vectors = ["v_a1", "v_a2", "v_b1", "v_b2", "v_cin", "v_s1", "v_s2", "v_cout"]

time = data[:, 0]

values = [data[:, 2 * i + 1] / 2.5 for i in range(len(vectors))]

fig, axs = plt.subplots(nrows=len(vectors), ncols=1, figsize=(10, 12))

# Plot each signal in a different subplot
for i, v in enumerate(vectors):
    axs[i].plot(time, values[i], label=v, color="blue")
    axs[i].set_ylabel("Voltage (V)")
    axs[i].set_title(f"{v} vs Time")
    axs[i].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the figure
plt.savefig(sys.argv[2])

fig_sum, axs_sum = plt.subplots(nrows=4, ncols=1, figsize=(10, 6))

axs_sum[0].plot(
    time, values[0] + values[1] * 2, label="v_a1 + 2*v_a2", color="blue"
)
axs_sum[0].set_ylabel("Voltage (V)")
axs_sum[0].set_title("v_a1 + 2*v_a2 vs Time")
axs_sum[0].grid(True)

axs_sum[1].plot(
    time, values[2] + values[3] * 2, label="v_b1 + 2*v_b2", color="blue"
)
axs_sum[1].set_ylabel("Voltage (V)")
axs_sum[1].set_title("v_b1 + 2*v_b2 vs Time")
axs_sum[1].grid(True)

axs_sum[2].plot(time, values[4], label="v_cin", color="blue")
axs_sum[2].set_ylabel("Voltage (V)")
axs_sum[2].set_title("v_cin vs Time")
axs_sum[2].grid(True)

axs_sum[3].plot(
    time,
    values[5] + values[6] * 2 + values[7] * 4,
    label="v_s1 + 2*v_s2 + 4*v_cout",
    color="blue",
)
axs_sum[3].set_ylabel("Voltage (V)")
axs_sum[3].set_title("v_s1 + 2*v_s2 + 4*v_cout vs Time")
axs_sum[3].grid(True)

plt.tight_layout()

plt.savefig(sys.argv[3])
