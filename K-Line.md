## Early P2 Vehicles (CEM-B)

The OBD-II CAN busses are separate from the rest of the vehicle's system, you must tell the CEM to connect them using the k-line interface. If you connect to to the CAN network elsewhere you won't need to do this.

```
Below are tested for accessing high speed CAN bus, but might also work for low speed CAN bus.

10400bps K-line. No initializing

84 40 13 B2 F0 03 7C (Connect CAN relay)
83 13 40 F2 F0 B8
84 40 13 B2 F0 03 7C (Keep alive every 4 seconds. If not the CAN line will be disconnected.)
83 13 40 F2 F0 B8
...
...
84 40 13 B2 F0 00 79 (Disconnect CAN relay)
83 13 40 F2 F0 B8

84: 80 + length of command behind addresses
40: Target address, CEM on K-line bus
13: Source address, Tester
B2: Activation command
F0: Parameter
03: Parameter
7C: Checksum
```
