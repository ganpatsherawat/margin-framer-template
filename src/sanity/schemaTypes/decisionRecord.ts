export default {
  name: 'decisionRecord',
  title: 'Decision Record',
  type: 'document',
  fields: [
    {
      name: 'quarterYear',
      title: 'Quarter & Year (e.g. Q1 2027)',
      type: 'string',
      initialValue: 'Q1 2027'
    },
    {
      name: 'title',
      title: 'Section Title',
      type: 'string',
      initialValue: 'The not-now list'
    },
    {
      name: 'items',
      title: 'Decision Items',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            { name: 'text', title: 'Initiative / Decision', type: 'string' },
            { 
              name: 'status', 
              title: 'Status', 
              type: 'string', 
              options: { 
                list: [
                  { title: 'Not Now (Stop)', value: 'not_now' },
                  { title: 'Funded (Keep)', value: 'funded' }
                ] 
              } 
            },
            { name: 'tag', title: 'Tag Label (e.g. Fund)', type: 'string' }
          ]
        }
      ]
    },
    {
      name: 'summaryStats',
      title: 'Summary Stats (e.g. 3 not now · 2 funded)',
      type: 'string',
      initialValue: '3 not now · 2 funded'
    }
  ]
};
