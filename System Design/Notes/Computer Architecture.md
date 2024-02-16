# Storage
A byte is 8 bits and each bit can store a 0 or a 1. We can use these bits to represent information.
0011 0001 : could be the letter A.
## Disk
Disk = Persistent Storage, so it is saved with power loss. Data is stored and saved here; during computer use, we typically have a capacity for a disk that is measured.  We typically see Disks in the form of Memory Cards, HDD's and SSD's (ordered in speed)

| Size | Bytes |
| ---- | ---- |
| MB | $10^6$ |
| GB | $10^9$ |
| TB | $10^{12}$ |
Reading and writing from disk is typically measured in milliseconds $ms$ , which is around $10^{-3}=1/10^3$ s.
## Ram
Random Access Memory, is a lot faster than disk but a lot more expensive in terms of space; and not persistent so when the machine turns off it is flushed and emptied.

Witing data to RAM is much faster than writing to disk. It would take would typically be measured in terms of micro-seconds $μ$'s which is $10^{-6}$ = $1/10^6$ ; basically a fraction of a second. One, one millionth of a second.

Ram can 10, 100, 1000x faster than disk depending on the context.
# CPU

The ram and disk cannot talk to each-other, so we give the CPU the tasks of writing and reading information to/from RAM or Disk. How much time it takes the CPU to perform these operations is the speed of the storage form.

Performs code and computations on data that it reads, by reading the code from ram or memory. The code and data could be in either the disk or ram.
![ ](assets/Pasted%20image%2020240216001531.png)

## Cache
While the ram is pretty fast at measurements of microseconds, if we want to go faster we can use the cache. The Cache is typically a component that is not separate from the CPU itself.

It is typically measured in terms of MB.

It is used to speed up read and write operations from ram, and this is possible because reading and writing from the cache is in the order of magnitude in speed of nanoseconds $ns$ which is $10^{-9}=1/10^9$ which is one-billionth of a second.

So it's faster, but stores a LOT less data. The Cache is typically used as a substitution for the ram. **What the CPU typically does is it chooses portions of the ram that we are writing and reading from frequently and moves it to the cache for faster access.**

**This too is not persistent data.**
