export interface ServiceItem {
  slug: string;
  numberCode: string;
  title: string;
  duration: string;
  priceFrom: string;
  summary: string;
  deliverables?: string[];
  thumbnailImage: string;
}

export interface CaseStudyItem {
  slug: string;
  title: string;
  industry: string;
  year: string;
  metricValue: string;
  metricLabel: string;
  headline: string;
  summary: string;
  coverImage: string;
  featured?: boolean;
}

export interface TestimonialItem {
  quote: string;
  author: string;
  initials: string;
  role: string;
  company: string;
  image: string;
}

export interface DecisionItem {
  text: string;
  status: 'not_now' | 'funded';
  tag?: string;
}

export const siteData = {
  brandName: 'Margin',
  tagline: 'Strategy & growth advisory',
  metaDescription: 'A two-partner strategy and growth advisory for B2B companies between $5M and $50M in revenue. We find the few decisions that matter, make them with you, and stay until they are working.',
  consultationNote: 'Thirty minutes with a partner. Free.',
  availability: 'BOOKING FROM JANUARY 2027',
  contactEmail: 'hello@margin.example',
  contactPhone: '+44 20 0000 0000',
  locations: 'London / Lisbon / Remote.',
  
  hero: {
    headline: 'We help growing companies decide what to stop doing.',
    subhead: 'Two partners, four clients at a time. We help you decide what matters, then stay until it works.',
    ctaText: 'Book an intro call',
    heroImage: '/images/d0SjRqtyPUYrbCUcZNSkemidbEo.jpg',
    heroImageAlt: 'A team meets around a table in a glass-walled meeting room at night.'
  },

  decisionRecord: {
    header: 'DECISION RECORD · Q1 2027',
    title: 'The not-now list',
    items: [
      { text: 'Enter the German market', status: 'not_now' },
      { text: 'Rebuild the ICP around retention', status: 'funded', tag: 'FUND' },
      { text: 'Rebrand before the Series B', status: 'not_now' },
      { text: 'Move pricing to annual contracts', status: 'funded', tag: 'FUND' },
      { text: 'Hire three more SDRs', status: 'not_now' }
    ] as DecisionItem[],
    stats: '3 NOT NOW · 2 FUNDED',
    cardImage: '/images/sEDxW3pFmiyamPRS8yfbtkGlm9g.jpg',
    cardImageAlt: 'A consultant writes the word ‘feedback’ on a whiteboard during a workshop.'
  },

  clientMarquee: [
    'fernhill',
    'Oakmont Health',
    'quarry/labs',
    'TIDEwater',
    'HALWARD',
    'kestrel'
  ],

  services: [
    {
      slug: 'positioning',
      numberCode: '01',
      title: 'Positioning',
      duration: '6 WEEKS',
      priceFrom: 'FROM $24,000',
      summary: 'Sharpen your point of view, identify your ideal customer profile, and align every sales conversation around how you uniquely win.',
      deliverables: [
        'Customer interview insights and win/loss audit',
        'Competitive differentiation thesis',
        'Core messaging matrix and narrative script',
        'Sales battlecard and qualification rubric'
      ],
      thumbnailImage: '/images/9x7V9MRIqEpblmsCVq3LlIRv0zM.jpg'
    },
    {
      slug: 'go-to-market',
      numberCode: '02',
      title: 'Go-to-market',
      duration: '8–10 WEEKS',
      priceFrom: 'FROM $38,000',
      summary: 'Rebuild your commercial engine. We align marketing demand, outbound focus, and customer success around retention and deal velocity.',
      deliverables: [
        'Commercial pipeline architecture',
        'Inbound and outbound playbooks',
        'Pricing packaging and contract transition roadmap',
        'RevOps dashboard and metric governance'
      ],
      thumbnailImage: '/images/sb6sFRPJvbDRjPVCNIhfoMF48.jpg'
    },
    {
      slug: 'advisory',
      numberCode: '03',
      title: 'Advisory',
      duration: '6 MONTHS MINIMUM',
      priceFrom: 'FROM $8,000 / MO',
      summary: 'An embedded strategic advisor directly with founders. We join leadership decisions, review major bets, and hold the line on focus.',
      deliverables: [
        'Weekly executive strategic sparring sessions',
        'Continuous decision governance and veto reviews',
        'Board deck preparation and narrative refinement',
        'Quarterly focus planning and stop-doing lists'
      ],
      thumbnailImage: '/images/3VQynPXYJkfR1omKmA1DVIAlKQI.jpg'
    }
  ] as ServiceItem[],

  featuredCase: {
    slug: 'fernhill',
    client: 'FERNHILL',
    industry: 'FREIGHT SOFTWARE',
    year: '2025',
    metricValue: '+41%',
    metricLabel: 'more qualified pipeline, two quarters after Fernhill stopped selling to everyone.',
    readText: 'Read the case'
  },

  caseStudies: [
    {
      slug: 'fernhill',
      title: 'Fernhill',
      industry: 'FREIGHT SOFTWARE',
      year: '2025',
      metricValue: '+41%',
      metricLabel: 'Qualified pipeline',
      headline: 'Narrowing the ICP to expand revenue velocity',
      summary: 'How focusing exclusively on high-retention enterprise logistics operators transformed deal cycles from 9 months to 45 days.',
      coverImage: '/images/dlrUWNpE3qg6yY2mt4QEw7q9pHM.jpg',
      featured: true
    },
    {
      slug: 'oakmont-health',
      title: 'Oakmont Health',
      industry: 'CLINIC SOFTWARE',
      year: '2025',
      metricValue: '2.3×',
      metricLabel: 'Enterprise win rate',
      headline: 'From commodity tool to clinical workflow backbone',
      summary: 'Restructuring enterprise pricing and stopping custom feature requests to double win rates against legacy health conglomerates.',
      coverImage: '/images/7i4qol44iSB6jMEujzXAV7BIrk8.jpg'
    },
    {
      slug: 'tidewater',
      title: 'Tidewater Studio',
      industry: 'ARCHITECTURE',
      year: '2026',
      metricValue: '+33%',
      metricLabel: 'Average project fee',
      headline: 'Moving from RFP fee competition to premium retained masterplans',
      summary: 'Turning down speculative pitch requests to command top-tier advisory retainers across major urban development bids.',
      coverImage: '/images/OZvY9GNTme626gh0nzhY3XZ3MA.jpg'
    }
  ] as CaseStudyItem[],

  testimonial: {
    quote: '“Nora talked us out of a rebrand. It was the most valuable thing anyone told us that year.”',
    author: 'Elena Sousa',
    initials: 'ES',
    role: 'Founder',
    company: 'Tidewater Studio',
    image: '/images/OZvY9GNTme626gh0nzhY3XZ3MA.jpg'
  } as TestimonialItem,

  ctaBanner: {
    badge: 'BOOKING FROM JANUARY 2027',
    headline: 'Tell us what’s stuck.',
    subhead: 'Thirty minutes with a partner. Free, and useful either way.',
    ctaButton: 'Book an intro call'
  },

  footer: {
    disclaimer: 'Client names, logos, figures, prices and testimonials on this site are samples. Replace them before launch.',
    copyright: '© 2026 MARGIN ADVISORY',
    styleGuide: '/style-guide'
  }
};
