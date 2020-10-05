for j in $(seq 1 5); do
for i in $(seq 10 99 | sort -r); do xrandr --output VGA-1 --gamma 0.$i:0:0; done
for i in $(seq 10 99); do xrandr --output VGA-1 --gamma 0.$i:0:0; done
for i in $(seq 10 99 | sort -r); do xrandr --output VGA-1 --gamma 0:0.$i:0; done
for i in $(seq 10 99); do xrandr --output VGA-1 --gamma 0:0.$i:0; done
for i in $(seq 10 99 | sort -r); do xrandr --output VGA-1 --gamma 0:0:0.$i; done
for i in $(seq 10 99); do xrandr --output VGA-1 --gamma 0:0:0.$i; done
done
xrandr --output VGA-1 --gamma 1:1:1
