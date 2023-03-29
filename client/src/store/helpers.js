// eslint-disable-next-line no-unused-vars
const paths = {
  root: '/api',
  items: '/api/items',
  getItemUrl(id) {
    return `/api/items/${id}`;
  },
};

export default paths;
