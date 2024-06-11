import React from 'react';
import axios from 'axios';

const Test = ({ }) => {
  const [listing, setListing] = React.useState('');
  const [list, setList] = React.useState([]);

  const handleListingUpdate = (e) => {
    setListing(e.target.value)
  }

  const handleSubmit = () => {
    const body = {
      listing: listing,
    };
    axios.post('/test/postListing', body);
    setListing('');
    fetchListings()
  };

  const fetchListings = () => {
    axios.get('/test/getListings')
      .then((res) => {
        setList(res.data);
      });
  };

  return (
    <div>
      <input value={listing} onChange={handleListingUpdate}/>
      <button onClick={handleSubmit}>Submit</button>

      <div class="testListings">
        {list.map((object, i) => <div key={i}>{object.listing}</div>)}
      </div>
    </div>
  );
};

export default Test;