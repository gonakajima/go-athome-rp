import React from 'react';
import Header from './Header';
import Main from './Main';
import Lineup from './Lineup';

class App extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Main />
        <Lineup />
      </div>
    );
  }
}

export default App;
