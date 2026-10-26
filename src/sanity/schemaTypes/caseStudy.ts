export default {
  name: 'caseStudy',
  title: 'Case Study',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Company / Project Name',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'industry',
      title: 'Industry / Domain',
      type: 'string'
    },
    {
      name: 'year',
      title: 'Engagement Year',
      type: 'string'
    },
    {
      name: 'metricValue',
      title: 'Primary Metric (e.g. +41%, 2.3x)',
      type: 'string'
    },
    {
      name: 'metricLabel',
      title: 'Metric Label (e.g. Qualified pipeline)',
      type: 'string'
    },
    {
      name: 'headline',
      title: 'Outcome Headline',
      type: 'string'
    },
    {
      name: 'overview',
      title: 'Overview',
      type: 'text'
    },
    {
      name: 'theChallenge',
      title: 'The Challenge',
      type: 'text'
    },
    {
      name: 'theStrategy',
      title: 'The Strategy & Hard Choices',
      type: 'text'
    },
    {
      name: 'coverImage',
      title: 'Cover Image',
      type: 'image',
      options: { hotspot: true }
    },
    {
      name: 'featured',
      title: 'Feature as Hero Highlight',
      type: 'boolean',
      initialValue: false
    },
    {
      name: 'order',
      title: 'Display Order',
      type: 'number'
    }
  ]
};
