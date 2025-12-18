app.get('/healthz', async (req, res) => {
  try {
    await pool.query('SELECT 1'); // Thử gửi một câu lệnh truy vấn đơn giản
    res.status(200).send('OK');
  } catch (err) {
    res.status(500).send('Not Ready');
  }
});
app.get('/healthz', async (req, res) => {
  try {
    await pool.query('SELECT 1'); // Thử gửi một câu lệnh truy vấn đơn giản
    res.status(200).send('OK');
  } catch (err) {
    res.status(500).send('Not Ready');
  }
});
