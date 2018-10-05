const rp = require("request-promise");
const url = `https://www.kijiji.ca/b-room-rental-roommate/city-of-toronto/c36l1700273?ad=offering&price=__1200&furnished=1`;
rp(url).then(response => console.log(response));
