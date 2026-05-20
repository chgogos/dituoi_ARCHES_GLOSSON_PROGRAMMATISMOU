import platform
import psutil


system_info = platform.uname()

print("Hardware:")
print(f"System: {system_info.system}")
print(f"Release: {system_info.release}")
print(f"Version: {system_info.version}")
print(f"Node Name: {system_info.node}")
print(f"Machine: {system_info.machine}")

cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
logical_cpu_count = psutil.cpu_count(logical=True)

print("\nCPU Information:")
print(f"Processor: {system_info.processor}")
print(f"Physical Cores: {cpu_count}")
print(f"Logical Cores: {logical_cpu_count}")

memory_info = psutil.virtual_memory()

print("\nMemory Information:")
print(f"Total Memory: {memory_info.total} bytes")
print(f"Available Memory: {memory_info.available} bytes")
print(f"Used Memory: {memory_info.used} bytes")
print(f"Memory Utilization: {memory_info.percent}%")
