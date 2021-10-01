package main

import "fmt"

type Robot struct {
	name string
	height int
}

func (r Robot) String() string{	
	return fmt.Sprintf("name: %s, height: %d",r.name, r.height)
}

func main() {
	r0 := Robot{name: "Optimus Prime", height: 100}
	fmt.Println(r0)

	var r1 Robot
	r1.name = "Optimus Prime"

	r2 := Robot{name: r1.name}
	fmt.Println(r2.name)

	r3 := Robot{r1.name, 100}
	fmt.Println(r3.name)

	r4 := new(Robot)
	r4.name = "Optimus Prime"

	r5 := &Robot{}
	r5.name = r1.name
	fmt.Println(r5.name)


}