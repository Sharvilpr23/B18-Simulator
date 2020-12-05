all: b18
b18: b18.cpp
	g++ -o b18 b18.cpp
clean:
	rm rf *.o *.d core b18