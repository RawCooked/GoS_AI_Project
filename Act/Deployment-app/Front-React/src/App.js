import React, { useState, useEffect } from 'react';
import './App.css'; // Import the CSS file

function App() {
  const [parents, setParents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchParents = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/parents/?format=json');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setParents(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchParents();
  }, []);

  if (loading) return <div className="loading">Loading data...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="app">
      <h1>Parent-Child Management</h1>
      <div className="parents-container">
        {parents.map(parent => (
          <div key={parent.id} className="parent-card">
            <div className="parent-header">
              <h2>{parent.first_name} {parent.last_name}</h2>
              <div className="parent-contacts">
                <span>📧 {parent.email}</span>
                <span>📞 {parent.phone_number}</span>
              </div>
            </div>

            <div className="children-section">
              <h3>Children ({parent.children.length})</h3>
              {parent.children.length > 0 ? (
                <ul className="children-list">
                  {parent.children.map(child => (
                    <li key={child.id} className="child-item">
                      <div className="child-info">
                        <strong>{child.first_name} {child.last_name}</strong>
                        <span>Born: {new Date(child.birth_date).toLocaleDateString()}</span>
                      </div>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="no-children">No children registered</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;