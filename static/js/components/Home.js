require('../../stylesheets/main.scss')

import React, { Component } from 'react'
import PropTypes from 'prop-types';

class Home extends Component {

  render() {
    var randomNumberOfPeople = Math.round( Math.random() * 1000 )
    return (
      <div className='landing-contents-container'>
        <div className='landing-header'>
        We're here to help you hold your elected officials accountable.
        </div>
        <div className='landing-subheader'>
          { randomNumberOfPeople } people have pledged to vote for a brand new congress.
        </div>
        <div className='landing-btn-container'>
          <div className='btn secondary-btn'>
            Learn More
          </div>
          <div className='btn primary-btn'>
            Get Started
          </div>
        </div>
      </div>
    )
  }
}

export default Home