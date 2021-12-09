import React from 'react';
import axios from 'axios';
 
class User extends React.Component {
  constructor(props){
    super(props)

    this.state ={
      Semester: '',
      Year: '',
      Student: '',
      Courses: '',
      Created: ''

    }
  }

  changeHandler = e =>{
    this.setState({[e.target.name]: e.target.value})
  }

  submitHandler = e =>{
    e.preventDefault()
    console.log(this.state)
    axios.post('http://167.99.3.85:8004/advising_form/{id}', this.state)
      .then(response =>{
        console.log(response)
      })
      .catch(error =>{
        console.log(error)
      })
  }


  render() {
    const {Semester, Year, Student, Courses, Created} = this.state
    return (
      <div>
        <form onSubmit = {this.submitHandler}>
          <span>
            <input className="mb-2 form-control semesterIn" type="text" name="Semester" value={Semester} onChange={this.changeHandler} placeholder="Semester"/>
            <input className="mb-2 form-control yearIn" type="text" name="Year" value={Year} onChange={this.changeHandler} placeholder="Year"/>
            <input className="mb-2 form-control studentIn" type="text" name="Student" value={Student} onChange={this.changeHandler} placeholder="Student"/>
            <input className="mb-2 form-control courseIn" type="text" name="Courses" value={Courses} onChange={this.changeHandler} placeholder="Courses"/>
            <input className="mb-2 form-control createIn" type="text" name="Created" value={Created} onChange={this.changeHandler} placeholder="Created"/>
            <button className="btn btn-outline-primary mx-2" style={{'borderRadius':'50px', "font-weight":"bold"}} type="submit">Add Form</button>
          </span>
        </form>
      </div>
    )
  }
}
 
export default User;
