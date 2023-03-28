export default function Profile(props) {
    console.log(props);

    return (
        <>
            <h2>{props.name}</h2>
            <img src={props.imgUrl} />
            {props.children}
        </>
    );
}