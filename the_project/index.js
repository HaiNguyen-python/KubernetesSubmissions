app.get('/healthz', async (req, res) => {
  try {
    await pool.query('SELECT 1'); // Kiểm tra kết nối tới Postgres
    res.status(200).send('Healthy');
  } catch (err) {
    res.status(500).send('Not Connected to DB');
  }
});
