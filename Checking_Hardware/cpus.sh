numactl --hardware
numactl --show


#Automatic kernel numa balancing? [1=yes, 0=no]
less /proc/sys/kernel/numa_balancing
sysctl kernel.numa_balancing=0
# Pero no se si deberia ser 0 o 1...
