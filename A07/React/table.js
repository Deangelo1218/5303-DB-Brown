import React, { Component } from 'react';
import Table from 'react-bootstrap/Table' 
 
 
class Listing extends Component {
 
    constructor(props) {
        super(props)   
        this.state = {
            records: []
        }
         
    }
 
    componentDidMount() {
        fetch('http://167.99.3.85:8004/forms/')
            .then(response => response.json())
            .then(records => {
                this.setState({
                    records: records
                })
            })
            .catch(error => console.log(error))
    }
 
    renderListing() {
        let recordList = []
        this.state.records.map(record => {
            return recordList.push(
                <Table striped bordered hover variant="dark">
                    <thead>
                    <tr>
                    <th>#</th>
                    <th >Name</th>
                    <th >Year</th>
                    <th >Semester</th>
                    <th >Course</th>
                    <th >Date Created</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                    <td>1</td>
                    <td>{record.Semester}</td>
                    <td>{record.Year}</td>
                    <td>{record.Student}</td>
                    <td>{record.Courses}</td>
                    <td>{record.Created}</td>
                    </tr>
                    </tbody>
            </Table>  
            )
        });
 
        return recordList;
    }
 
    render() {
        return (
            <ul>
                {this.renderListing()}
            </ul>
        );
    }
}
 
export default Listing;

