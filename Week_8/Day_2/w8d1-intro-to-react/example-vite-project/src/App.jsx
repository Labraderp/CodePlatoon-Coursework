export default function App() {
  const profiles = [
    { name: 'Benjamin Cohen', imgUrl: "https://via.placeholder.com/600x400" },
    { name: 'Adam Cahan', imgUrl: "https://via.placeholder.com/600x400" },
    { name: 'Slavoj Zizek', imgUrl: "https://via.placeholder.com/600x400" }
  ]

  return <ProfileContainer profiles={profiles} />;
}

// same definition as before
function Profile({ name, imgUrl }) {
  return (
    <div className="profile">
      <h2>{name}</h2>
      {(imgUrl && imgUrl.length === 0) ? <img src={imgUrl} /> : null}
    </div>
  );
}


function ProfileContainer({ profiles }) {
  const profilesAsComponents = [];

  for (const { name, imgUrl } of profiles) {
    profilesAsComponents.push(<Profile name={name} imgUrl={imgUrl} />)
  }

  return (
    <div>
      <h1>Profiles</h1>
      <div id="profiles_container">
        {profilesAsComponents}
      </div>
    </div>
  )
}