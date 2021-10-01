package main

import "fmt"

type Skills struct {
	speak string 
}

func (s Skills) Speak()  {
	fmt.Println(s.speak)	
}

type Robot struct {
	name string // 姓名
	height int // 身高
	Skills
}

func (r Robot) Speak() {	
	fmt.Printf("My name is %s, ",r.name)
	r.Skills.Speak()
}

func main() {
	skill := Skills{speak: "hello !"}
	skill.Speak()
	
	robot := Robot{
		name: "Optimus Prime",
		Skills: skill,
	}
	robot.Speak()
}
