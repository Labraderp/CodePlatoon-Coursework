import '../css/homepage.css';
import InventoryItem from './InventoryItem';

export default function HomePage({ inventory }) {
  return (
    <>
      <h2> Inventory </h2>
      <div class="title_container">
        {
          inventory.map(props => <InventoryItem {... props} />)
        }
      </div>
    </>
  );
}