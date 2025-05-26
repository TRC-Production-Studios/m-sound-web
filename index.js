const express = require('express');
const fs = require('fs');
const app = express();
const PORT = process.env.PORT || 3000;

// Get users
const getLicensedUsers = () => {
  const data = fs.readFileSync('licensed_users.json');
  return JSON.parse(data).users;
};

// Save users
const saveLicensedUsers = (users) => {
  fs.writeFileSync('licensed_users.json', JSON.stringify({ users }, null, 2));
};

// ✅ Check if user is licensed
app.get('/check', (req, res) => {
  const userId = parseInt(req.query.userId);
  if (!userId) {
    return res.status(400).json({ error: 'Missing userId' });
  }

  const licensedUsers = getLicensedUsers();
  res.json({ licensed: licensedUsers.includes(userId) });
});

// ➕ Add a licensed user
app.get('/add', (req, res) => {
  const userId = parseInt(req.query.userId);
  if (!userId) {
    return res.status(400).json({ error: 'Missing userId' });
  }

  const licensedUsers = getLicensedUsers();

  if (!licensedUsers.includes(userId)) {
    licensedUsers.push(userId);
    saveLicensedUsers(licensedUsers);
    res.json({ success: true, message: `User ${userId} added.` });
  } else {
    res.json({ success: false, message: `User ${userId} already licensed.` });
  }
});

// Root
app.get('/', (req, res) => {
  res.send('License API is running.');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
